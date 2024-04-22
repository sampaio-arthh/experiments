<?php
error_reporting(E_ERROR | E_PARSE);

function db_insert($tableName, $data) {
    $db = new SQLite3('data.sqlite3');
    $columns = [];
    $values = [];
    foreach($data as $columnName => $value) {
        $columns[] = "`$columnName`";
        $values[] = "'".SQLite3::escapeString($value)."'";
    }
    $strColumns = implode(",",$columns);
    $strValues = implode(",",$values);
    $sql = "insert into `$tableName` ($strColumns) values ($strValues)";
    $resp = $db->exec($sql);
    if(!$resp) {
        $count = $db->querySingle("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='$tableName'");
        if($count === 0) {
            $db->exec("CREATE TABLE `$tableName` ($strColumns)");
            $resp = $db->exec($sql);
        }
    }
    $lastId = $db->lastInsertRowID();
    $db->close();
    return $lastId;
}

function db_update($tableName, $data) {
    $db = new SQLite3('data.sqlite3');
    $columns = [];
    $id = $data["id"];
    $where = "rowid=$id";
    foreach($data as $columnName => $value) {
        if($columnName != "id") {
            $columns[] = "`".$columnName."`='".SQLite3::escapeString($value)."'";
        }
    }
    $strColumns = implode(",",$columns);
    $sql = "update `$tableName` set $strColumns where ($where)";
    if($db->exec($sql)) {
        return db_fetchForUpdate($tableName,$id);
    } else {
        return null;
    }
}

function db_delete($tableName, $ids) {
    $db = new SQLite3('data.sqlite3');
    $sql = "delete from `$tableName` where rowid in ($ids)";
    return $db->exec($sql);
}

function db_list($tableName) {
    $db = new SQLite3('data.sqlite3');
    $sql = "select rowid as id, * from `$tableName`";
    $resp = $db->query($sql);
    $header = [];
    $rows = [];
    if($resp) {
        for($i=1; $i<$resp->numColumns(); $i++) {
            $header[] = $resp->columnName($i);
        }
        $row = $resp->fetchArray(SQLITE3_NUM);
        while($row) {
            $id = array_shift($row);
            $rows[] = array( "id" => $id, "data" => $row);
            $row = $resp->fetchArray(SQLITE3_NUM);
        }
    }
    $db->close();
    return [ "header" => $header, "rows" => $rows ];
}

function db_fetchForUpdate($tableName, $id) {
    $db = new SQLite3('data.sqlite3');
    $sql = "select rowid as id, * from `$tableName` where rowid = $id";
    $row = $db->querySingle($sql,true);
    $db->close();
    return $row;
}

function crudJS() { 
    return <<<'EOT'
        const ft = (function(){
            const HTML_NS = "http://www.w3.org/1999/xhtml";
            const SVG_NS = "http://www.w3.org/2000/svg";
            function tagFactory(NS,tagName) {
                return function(...args) {
                    let element = document.createElementNS(NS,tagName);
                    function flatten(e) {
                        if(e !== null && e !== "" && e !== undefined) {
                            if(e.forEach) {
                                e.forEach(flatten);
                            } else {
                                if (e instanceof Node) {
                                    element.append(e);
                                } else if(e instanceof Object) {
                                    for(let k in e) {
                                        let v = e[k];
                                        if(v !== null) {
                                            let evname = (/^on(.+)$/.exec(k)||[])[1];
                                            if(evname) {
                                                element.addEventListener(evname,v);
                                            } else if(k === 'style') {
                                                for(let ks in v) {
                                                    element.style[ks] = v[ks];
                                                }
                                            } else {
                                                element.setAttribute(k,v);
                                            }
                                        }
                                    }
                                } else {
                                    element.append(document.createTextNode(e));
                                    element.normalize();
                                }
                            }
                        }
                    }
                    flatten(args);        
                    return element;
                }
            }
            return {
                html: new Proxy({}, {get:(target,name)=>(name in target)?target[name]:tagFactory(HTML_NS,name)}),
                svg: new Proxy({}, {get:(target,name)=>(name in target)?target[name]:tagFactory(SVG_NS,name)})
            }
        })();
        
        function icon(name) {
            const { i } = ft.html;
            return i({class:`fa fa-${name}`});
        }
        
        function redirect(params) {
            let l = window.location;
            if(params) {
                let p = new URLSearchParams(params);
                l.replace(l.origin + l.pathname + "?" + p.toString());
            } else {
                l.replace(l.origin + l.pathname);
            }
        }
        
        function getUrlInfo() {
            let l = window.location;
            let name = null;
            let params = new URLSearchParams(l.search);
            let cmd = params.get("cmd");
            let id = params.get("id");
            let p1 = l.pathname.lastIndexOf('/')+1;
            let p2 = l.pathname.lastIndexOf('.')
            if(p2 > 0) {
                name = l.pathname.substring(p1,p2);
            }
            return { name, cmd, id };
        }
        
        async function callApi(command, tableName, data) {
            let body;
            if(data instanceof FormData) {
                body = data;
            } else {
                body = new FormData();
                for(let k in data) {
                    body.set(k,data[k]);
                }
            }
            let headers = new Headers()
            headers.append("TABLE_NAME",tableName);
            headers.append("CMD",command);
            let options = { method: "POST", headers, body };
            let resp = await fetch("/crud.php", options);
            return await resp.json();
        }
        
        function createFormData(frm,id) {
            let formData = new FormData(frm);
            if(id) {
                formData.set("id",id);
            }
            frm.querySelectorAll("input[type=checkbox]:not(:checked)").forEach(cb=>formData.set(cb.name,0));
            return formData;
        }
        
        function db_create(frm,name) {
            frm.addEventListener("submit", ev=>{
                ev.preventDefault();
                callApi("create",name,createFormData(frm))
                    .then(t => {redirect({id:t.id})})
                ;
            });
            installMasks(frm);
        }
        
        function db_delete(name,ids) {
            callApi("delete",name,{ids})
                .then(t => {redirect()})
            ;
        }
        
        function setFormData(frm, data) {
            for(let element of frm) {
                let name = element.name;
                if(name) {
                    let value = data[name];
                    if(element.type == "checkbox") {
                        element.checked = (value==element.value || value == "on");
                    } else if(element.type == "radio") {
                        element.checked = (value==element.value);
                    } else {
                        if(value !== undefined && value !== null && value != NaN) {
                            element.value = value;
                        } else {
                            element.value = "";
                        }
                    }
                }
            }
        }
        
        function db_update(frm,name,id) {
            frm.addEventListener("submit", ev=>{
                ev.preventDefault();
                callApi("update",name,createFormData(frm,id))
                    .then(t => {redirect({id})})
                ;
            });
            installMasks(frm);
            callApi("fetchForUpdate",name,{id}).then(d => {
                setFormData(frm,d.data);
            });
        }
        
        function dataGrid(labels, header, rows) {
            const { table, thead, tbody, tr, td, th, button, input } = ft.html;
            let header2 = header.map(h=>labels.get(h));
        
            function editarClick(row) {
                redirect({cmd:"update",id:row.id});
            }
        
            return table({class:"table table-striped table-bordered align-middle"},
                thead(
                    tr(
                        th(),
                        header2.map(h=>(h&&(th(h))||"")),
                        th()
                    )
                ),
                tbody(
                    rows.map(row=>tr(
                        td({class:"text-center"},input({class:"form-check-input",type:"checkbox",value:row.id})),
                        row.data.map((cell,i)=>header2[i]?td(cell):""),
                        td({class:"d-flex gap-2 justify-content-evenly"},
                            button({class:"btn btn-outline-primary btn-sm d-flex align-items-baseline gap-1", onclick: ()=>editarClick(row)},icon("edit"),"Editar"),
                        )
                    ))
                )
            );
        }
        
        function db_retrieve(frm,name) {
            const { div, button } = ft.html;
            let tablePlaceholder = div();
            let btExclui;
        
            function excluirClick() {
                let cbs = tablePlaceholder.querySelectorAll("input[type=checkbox]:checked");
                let ids = [];
                cbs.forEach(cb=>ids.push(cb.value));
                if(cbs.length > 0) {
                    showModal("Exclusão de Registro",`Confirma a exclusão de ${cbs.length} registro${cbs.length>1?'s':''}?`)
                        .then(()=>{db_delete(name, ids.join(","))})
                        .catch(()=>{})
                    ;
                }
            }
        
            function habilitaBotoes() {
                let cbs = tablePlaceholder.querySelectorAll("input[type=checkbox]");
                if(cbs.length) {
                    btExclui.removeAttribute("disabled");
                } else {
                    btExclui.setAttribute("disabled","disabled");
                }
            }
        
            let labels = labelMap(frm);
        
            frm.replaceWith(div({class:"py-2"},
                tablePlaceholder,
                div({class:"d-flex gap-2 justify-content-evenly"},
                    button({class:"btn btn-outline-primary btn-sm d-flex align-items-baseline gap-1",onclick:()=>redirect({cmd:"new"})},icon("plus"),"Inclui"),
                    btExclui=button({class:"btn btn-outline-danger btn-sm d-flex align-items-baseline gap-1",onclick:excluirClick,disabled:"disabled"},icon("trash"),"Excluir"),
                )
            ));
        
            callApi("retrieve",name,frm).then(t=>{
                if(t.data.rows.length > 0) {
                    tablePlaceholder.replaceChildren(dataGrid(labels,t.data.header,t.data.rows));        
                    tablePlaceholder.querySelectorAll("input[type=checkbox]").forEach(cb=>{
                        cb.addEventListener("change",habilitaBotoes);
                    });
                } else {
                    redirect({cmd:"new"});
                }
            });
        }
        
        function initApplication() {
            let { name, cmd, id } = getUrlInfo();
            let frm = document.querySelector('form');
            if(cmd == "new") {
                db_create(frm,name);
            } else if(cmd == "update") {
                db_update(frm,name,id);
            } else {
                db_retrieve(frm,name,id);
            }
        }
        
        function showModal(title, message, cancelButtonText, okButtonText) {
            cancelButtonText = cancelButtonText || "Cancela";
            okButtonText = okButtonText || "OK";
        
            let { div, h5, button } = ft.html;
            let modalHandler;
            let btOk;
            let resolveFlag = false;
        
            return new Promise( (resolve,reject) => {
                function onclick(ev) {
                    if(ev.target == btOk) {
                        resolveFlag = true;
                    }
                    modalHandler.hide();
                }
                let modal = (
                    div({class:"modal", tabindex:"-1"},
                        div({class: "modal-dialog"},
                            div({class: "modal-content"},
                                div({class: "modal-header"},
                                    h5({class: "modal-title"},title),
                                    button({type:"button", class:"btn-close", onclick})
                                ),
                                div({class: "modal-body"},
                                    message
                                ),
                                div({class: "modal-footer"},
                                    button({type:"button", onclick, class:"btn btn-secondary"},cancelButtonText),
                                    btOk = button({type:"button", onclick, class:"btn btn-primary"},okButtonText)
                                ),
                            ),
                        )
                    )
                );
                modalHandler = new bootstrap.Modal(modal, {});
                modalHandler.show();
                modal.addEventListener("hidden.bs.modal", ev=>{
                    modal.remove();
                    modalHandler.dispose();
                    resolveFlag ? resolve() : reject();
                });
            });
        }
        
        const SYM_MASK = Symbol();
        const namedMasks = {
            "celular": { mask: "(00)00000-0000" },
            "cpf": { mask: "000.000.000-00" },
            "cep": { mask: "00000-000" },
        };
        
        function getFormTitle() {
            let main = document.querySelector("main");
            if(main) {
                let title = main.querySelector("h1,h2,h3,h4,h5");
                if(title) {
                    return title.textContent;
                }
            }
            return "";
        }
        
        function installMasks(frm) {
            let inputs = frm.querySelectorAll("[data-mask]");
            inputs.forEach(input=>{
                let options = namedMasks[input.dataset.mask];
                if(!options) {
                    options = { mask: input.dataset.mask };
                }
                input[SYM_MASK] = IMask(input,options);
            });
        }
        
        function labelMap(frm) {
            let m = new Map();
            let labels = frm.querySelectorAll("label");
            for(let label of labels) {
                let idElement = label.getAttribute("for");
                if(idElement) {
                    let e = document.getElementById(idElement);
                    if(e) {
                        if(e.type == 'radio' || e.type == 'password') {
                            continue;
                        }
                        let name = e.getAttribute("name");
                        let labelText = label.textContent.trim();
                        if(name && labelText) {
                            m.set(name,labelText);
                        }
                    }
                }
            }
            if(m.size == 0) {
                for(let e of frm) {
                    if(e.type != 'radio' && e.type != 'password') {
                        m.set(e.name,e.name);
                    }
                }
            }
            return m;
        }
        
        document.onreadystatechange = function () {
            if (document.readyState === 'interactive') {
                initApplication();
                document.querySelector('main').classList.remove("d-none");
            }
        }
    EOT;
}

function modelo($conteudo) {
    $js = crudJS();
    echo <<<EOT
        <html>
            <head>
                <title>CRUD</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                <script src="https://unpkg.com/imask"></script>
                <script>$js</script>
            </head>
            <body>
                <header>
                </header>
                <main class="d-none">$conteudo</main>
                <footer>
                </footer>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
            </body>
        </html>
    EOT;
}

if($_SERVER["REQUEST_METHOD"] == "POST") {
    $cmd = $_SERVER["HTTP_CMD"];
    $tableName = $_SERVER["HTTP_TABLE_NAME"];
    if($cmd == "create") {
        $id = db_insert($tableName,$_POST);
        echo json_encode(["status" => "OK", "id" => $id ]);
    }
    else if($cmd == "retrieve") {
        $data = db_list($tableName);
        echo json_encode(["status" => "OK", "data" => $data ]);
    }
    else if($cmd == "delete") {
        $ids = $_POST["ids"];
        $status = db_delete($tableName,$ids) ? "OK" : "ERROR";
        echo json_encode(["status" => $status]);
    }
    else if($cmd == "fetchForUpdate") {
        $id = $_POST["id"];
        $data = db_fetchForUpdate($tableName,$id);
        if($data) {
            echo json_encode(["status" => "OK", "data" => $data]);
        } else {
            echo json_encode(["status" => "ERROR"]);
        }
    }
    else if($cmd == "update") {
        $data = db_update($tableName,$_POST);
        if($data) {
            echo json_encode(["status" => "OK", "data" => $data]);
        } else {
            echo json_encode(["status" => "ERROR"]);
        }
    }
}

if($_SERVER["REQUEST_METHOD"] == "GET") {
    register_shutdown_function(function(){
        modelo(ob_get_clean());
    });
    ob_start();
}

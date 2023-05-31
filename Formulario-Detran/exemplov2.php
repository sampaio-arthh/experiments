<?php include 'crud.php'?>

<div class="container py-4">
    <h4>Cadastro Detran</h4>
    <form class="row g-3">
        <div class="col-md-12">
            <label for="inputNome4" class="form-label">Nome</label>
            <input type="text" class="form-control" name="nome" id="inputNome4">
        </div>
        <div class="col-md-12">
            <label for="inputNomeS4" class="form-label">Nome Social</label>
            <input type="text" class="form-control" name="nomeSocial" id="inputNomeS4" autocomplete="off">
        </div>
        <div class="col-7">
            <label for="inputIdentidade" class="form-label">Documento de Identidade</label>
            <input type="text" class="form-control" id="inputIdentidade" name="docId">
        </div>
        <div class="col-5">
            <label for="inputOrgao2" class="form-label">Órgão Expedidor</label>
            <input type="text" class="form-control" id="inputOrgao2" name="orgao">
        </div>
        <div class="col-md-12">
            <label for="inputCPF" class="form-label">CPF</label>
            <input type="text" class="form-control" name="cpf" id="inputCPF" data-mask="000.000.000-00">
        </div>
        <div class="col-md-7">
            <label for="inputState" class="form-label">Nacionalidade</label>
            <input id="inputNacionalidade" class="form-control" name="nacionalidade">
        </div>
        <div class="col-md-5">
            <label for="inputZip" class="form-label">Naturalidade</label>
            <input type="text" class="form-control" id="input" name="naturalidade">
        </div>
        <div class="col-md-7">
            <label for="inputTelefone" class="form-label">Telefone</label>
            <input id="inputTelefone" class="form-control" name="telefone" data-mask="(00)0000-0000">
        </div>
        <div class="col-md-5">
            <label for="inputCelular" class="form-label">Celular</label>
            <input type="text" class="form-control" id="inputCelular" name="celular" data-mask="(00)00000-0000">
        </div>
        <div class="col-md-12">
            <label for="inputEmail" class="form-label">E-mail</label>
            <input type="text" class="form-control" name="email" id="inputEmail">
        </div>
        <br>
        <div class="col-md-12">
            <label for="inputEndereco" class="form-label">Endereço</label>
            <input type="text" class="form-control" name="endereco" id="inputEndereco">
        </div>
        <div class="col-md-2">
            <label for="inputNum" class="form-label">Nº</label>
            <input type="text" class="form-control" name="num" id="inputNumero">
        </div>
        <div class="col-md-6">
            <label for="inputComplemento" class="form-label">Complemento</label>
            <input type="text" class="form-control" name="complemento" id="inputComplemento">
        </div>
        <div class="col-md-4">
            <label for="inputCep" class="form-label">CEP</label>
            <input type="text" class="form-control" name="cep" id="inputCep">
        </div>
        <div class="col-md-2">
            <label for="inputUf" class="form-label">UF</label>
            <input type="text" class="form-control" name="uf" id="inputUf">
        </div>
        <div class="col-md-6">
            <label for="inputCidade" class="form-label">Cidade</label>
            <input type="text" class="form-control" name="cidade" id="inputCidade">
        </div>
        <div class="col-md-4">
            <label for="inputBairro" class="form-label">Bairro</label>
            <input type="text" class="form-control" name="bairro" id="inputBairro">
        </div>
        <div class="col-12">
            <button type="submit" class="btn btn-primary">Sign in</button>
        </div>
    </form>
</div>

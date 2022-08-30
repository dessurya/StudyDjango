submitLogin = () => {
    let params = {}
    params.email = $('[name=email]').val()
    params.password = $('[name=password]').val()
    httpRequest(uri_login,'POST',params).then((res) => {
        alert(res.response.msg)
        if(res.response.login){
            window.location.reload()
        }
    })
    return false
}
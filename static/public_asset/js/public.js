httpRequest = (target, method, param) => {
    return new Promise(function(resolve, reject) {
        $.ajax({
            url: target,
            type: method,
            data: param,
            dataType: 'json',
            success : function(result) { 
                if (result.response.login == false) {
                    // loadingScreen(false)
                    alert(result.response.msg)
                    window.location.reload()
                }else{
                    resolve(result)
                }
            },
            error : function(err) {
                console.log(err)
                // loadingScreen(false)
                reject(err)
            }
        })
    })
}
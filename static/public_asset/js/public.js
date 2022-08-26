httpRequest = (target, method, param) => {
    return new Promise(function(resolve, reject) {
        $.ajax({
            url: target,
            type: method,
            data: param,
            dataType: 'json',
            success : function(result) { 
                if (result.response == false) {
                    alert(result.msg)
                    loadingScreen(false)
                }else{
                    resolve(result)
                }
            },
            error : function(err) {
                console.log(err)
                loadingScreen(false)
                reject(err)
            }
        })
    })
}
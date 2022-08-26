// page const statis
    const elem_list = '#list-user-contain-target'
    const elem_form = '#form-user-contain-target'
    const elem_nav = 'ul#custom-tabs-user-tab'
// page const statis

$( document ).ready(function() {
    getList(true)
});

getList = (firstPage) => {
    const elmTarget = elem_list
    let params = {}
    params.email = $(elmTarget+' .card-header [name=fillter_email]').val()
    params.name = $(elmTarget+' .card-header [name=fillter_name]').val()
    params.show = $(elmTarget+' .card-header [name=show]').val()
    params.order_by = $(elmTarget+' .card-header [name=order_by]').val()
    params.order_by_value = $(elmTarget+' .card-header [name=order_by_value]').val()
    params.halaman = 1
    if (firstPage == false) { params.halaman = $(elmTarget+' .card-header [name=halaman]').val() }
    httpRequest(uri_getlist,'GET',params).then((res) => {
        $(elmTarget+' .card-body table tbody').html('')
        $(elmTarget+' .card-header #halaman label b').html(res.response.last_page)
        $(elmTarget+' .card-header #halaman [name=halaman]').val(res.response.halaman)
        $(elmTarget+' .card-header #halaman [name=halaman]').attr('max',res.response.last_page)
        if (res.response.dataCount == 0) {
            $(elmTarget+' .card-body table tbody').html('<tr><td colspan="4" class="text-center">-- NOT FOUND DATA --</td></tr>')
        }else{
            let renders = ''
            $.each(res.response.data, (idx, row) => {
                renders += '<tr>'
                renders += '<td><div class="btn-group">'
                renders += '<span onclick="openData('+row.id+')" class="btn btn-sm btn-outline-info">Open</span>'
                renders += '<span onclick="deleteData('+row.id+')" class="btn btn-sm btn-outline-danger">Delete</span>'
                renders += '</div></td>'
                renders += '<td>'+row.name+'</td>'
                renders += '<td>'+row.email+'</td>'
                renders += '<td>'+row.created_at+'</td>'
                renders += '</tr>'
            })
            $(elmTarget+' .card-body table tbody').html(renders)
        }
    })
}

closeForm = () => {
    const elmTarget = $(elem_form+" form")
    elmTarget.hide()
    elmTarget.find('.card-header h3').html('')
    elmTarget.find('input').val(null)
}

activeForm = () => {
    $(elem_form+" form button[type=reset]").click()
    $(elem_nav+" #form-user-contain").click()
    const elmTarget = $(elem_form+" form")
    elmTarget.show()
}

addData = () => {
    const elmTarget = $(elem_form+" form")
    elmTarget.find('.card-header h3').html('Form Add Users')
    activeForm()
}

openData = (id) => {
    activeForm()
    httpRequest(uri_opendata,'GET',{'id':id}).then((res) => {
        const elmTarget = $(elem_form+" form")
        elmTarget.find('.card-header h3').html('Update User : <small>'+res.response.data.email+'</small>')
        elmTarget.find('[name=name]').val(res.response.data.name)
        elmTarget.find('[name=email]').val(res.response.data.email)
        elmTarget.find('[name=id]').val(res.response.data.id)
    })
}

deleteData = (id) => {
    let askConf = confirm('delete this data?')
    if (askConf) {
        httpRequest(uri_deletedata,'POST',{'id':id}).then((res) => {
            closeForm()
            getList(true)
            alert(res.response.msg)
        })
    }
}

submitForm = () => {
    const elmTarget = $(elem_form+" form")
    let params = {}
    params.name = elmTarget.find('[name=name]').val()
    params.email = elmTarget.find('[name=email]').val()
    params.id = elmTarget.find('[name=id]').val()
    httpRequest(uri_storedata,'POST',params).then((res) => {
        getList(true)
        openData(res.response.id)
    })
    return false
}
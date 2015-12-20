$(function(){
    // https://docs.djangoproject.com/en/1.8/ref/csrf/
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(
                        cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }  

    var csrftoken = getCookie('csrftoken');
    $(".request").click(function(event) {
        event.preventDefault();
        urlnext = this.getAttribute('urlnext')
        verb = this.getAttribute('verb')

        $.ajax({
            url: this.href,
            type: verb,
            success: function(result) {
                if (urlnext){
                    location.replace(urlnext);
                }
                else{
                    location.reload();
                }
            },
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
        });
        
        return false;
    }); 
});
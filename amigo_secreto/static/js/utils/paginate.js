$(function() {
    // this function makes the click the href is a click 
    // on the search button
    
    // is very useful on django paginate
    $("ul.pager a").on("click", function(e){
      e.preventDefault();
      var form = $("#form-search");
      var url_action = form.attr('action');
      form.attr('action', url_action + $(this).attr('href'));
      form.trigger('submit');
    });
});

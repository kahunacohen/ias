$.fn.isOnScreen = function(){
    var element = this.get(0);
    var bounds = element.getBoundingClientRect();
    return bounds.top < window.innerHeight && bounds.bottom > 0;
}

$.getQuery = function( query ) {
    query = query.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var expr = "[\\?&]"+query+"=([^&#]*)";
    var regex = new RegExp( expr );
    var results = regex.exec( window.location.href );
    if( results !== null ) {
        return results[1];
        return decodeURIComponent(results[1].replace(/\+/g, " "));
    } else {
        return false;
    }
};

$("div#ct").jscroll({
    contentSelector: "#ct", 
    nextSelector: ".pagination:last a#next", 
    autoTrigger:true,
    callback: function() {
        $(".pagination").slice(0, -1).remove();    
    }
});

$(document).scroll( $.debounce( 250, function() {
    $('.content').each( function() {
        var $content = $(this);
        if( $content.isOnScreen() ) {
            var curPage = $content.data("page");
            if( curPage !==  parseInt($.getQuery("page"))) {
                history.pushState({}, "", "?page=" + curPage);
            }
        } 
    });
}));

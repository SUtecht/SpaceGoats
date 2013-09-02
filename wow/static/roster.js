$(document).ready(function(){
    $('.alt').hide();
    $('.toggleminus').hide();
    $('.toggle').click(function(){
        var name = '.' + this.classList[0];
        $(name+'.alt').toggle();
        $(name+'.toggleminus').toggle();
        $(name+'.toggleplus').toggle();
    });
});

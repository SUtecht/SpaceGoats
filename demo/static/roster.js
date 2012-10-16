$(document).ready(function(){
    $('.alt').hide();
    $('.toggle').click(function(){
        var name = '.' + this.classList[0];
        $(name+'.alt').toggle();
    });
});

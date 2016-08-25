(function () {
  $(document).ready(function(){
    $(document).on("click", ".captcha-reload, .captcha-image", function(){
      var img = $('img.captcha-image', $(this).parent());
      img.attr('src', img.attr('src').split('?', 1)+'?update=1&'+Math.random());
      return false;
    });
  });
}).call(this);

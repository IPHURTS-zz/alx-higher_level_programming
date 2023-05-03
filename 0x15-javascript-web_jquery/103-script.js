<!DOCTYPE html>
<html>
  <head>
    <title>Translation Example</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
      $(document).ready(function() {
        $('#btn_translate').click(translateHello);
        $('#language_code').keydown(function(event) {
          if (event.keyCode == 13) {
            translateHello();
          }
        });
        
        function translateHello() {
          var language_code = $('#language_code').val();
          var url = 'https://fourtonfish.com/hellosalut/?lang=' + language_code;
          
          $.getJSON(url, function(data) {
            $('#hello').text(data.hello);
          });
        }
      });
    </script>
  </head>
  <body>
    <label for="language_code">Language code:</label>
    <input type="text" id="language_code">
    <input type="button" id="btn_translate" value="Translate">
    <div id="hello"></div>
  </body>
</html>

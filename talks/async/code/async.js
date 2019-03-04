$("#ok-btn").on('click', function() {
  // do some stuff here then post some data
  $.post('/foo', json, function(data) {
      // on success continue doing stuff here
  })
  .fail(function(response) {
      // on error, do some cleanup here
  })
);

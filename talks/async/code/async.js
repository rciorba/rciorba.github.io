$("#ok-btn").on('click', function() {
  // disable the button, and render a spinner
  $.post('/foo', json, function(data) {
      // close the dialog
  })
  .fail(function(response) {
      // re-enable dialog, hide spinner
  })
);

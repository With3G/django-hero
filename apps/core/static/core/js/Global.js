var Global = {
  init: function () {
    this.setListeners();
  },

  setListeners: function () {
    var self = this;

//    $('.alert-fadeOut').delay(5000).fadeOut('slow');

    // Tip para eliminar un modal una vez oculto.
    $(document).on('hidden.bs.modal', '.modal', function (e) {
      $(this).remove();
    });

    //Modal confirm action
    $(document).on('click', '.modal-confirm-action', function(e) {
      self.modalConfirmAction($(this), e)
    });

  },


  /**
   *
   */
  modalConfirmAction: function(element, e) {
     var self = this;
     e.preventDefault()

     $.ajax({
        method: 'POST',
        url: BASE_URL + '/modal_confirm_action/',
        data: {
          csrfmiddlewaretoken: jQuery('[name=csrfmiddlewaretoken]').val(),
          action_url: element[0].href,
          action_text: element.data('modal-text')
        },
        dataType: 'Html'
     }).done(function(response, data) {
         $('body').append(response);
         $('#modal-confirm-action').modal('show');
     }).fail(function(error) {
        //ERROR
        alert("ERROR modalConfirmAction()")
     });
  }

}

$(document).ready(function () {
  Global.init();
});

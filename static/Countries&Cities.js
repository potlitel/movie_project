;(function(Utils) {
  'use strict';
 
 var url;
 var selectedItemId;

var response_cache = {};


  function GetMunicipalities(post_primary_key){
        $.ajax({
            url : "ciudades/", // the endpoint
            type : "POST", // http method
            data : { postpk : post_primary_key }, // data sent with the delete request
            success : function(json_response) 
            {
                // hide the post
              // $('#post-'+post_primary_key).hide(); // hide the post on success
              // console.log(json_response);
              $('#id_ciudad').empty()
              for (var i in json_response) 
              {
                 //console.log(json_response[i].fields.nombre + json_response[i].pk);
                $('#id_ciudad').append($('<option>', { 
                                value: json_response[i].pk,
                                text: json_response[i].fields.nombre 
                        }));
              }
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                $('#results').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
  };

Utils.disableButtons = function(editBtn, deleteBtn){
	$("#" + editBtn).attr('disabled','disabled');
 	$("#" + deleteBtn).attr('disabled','disabled');
}

Utils.disableButtonsSAI = function(editBtn, deleteBtn, aprovedBtn, evaluateBtn){
  $("#" + editBtn).attr('disabled','disabled');
  $("#" + deleteBtn).attr('disabled','disabled');
  $("#" + aprovedBtn).attr('disabled','disabled');
  $("#" + evaluateBtn).attr('disabled','disabled');
}

Utils.table_tr_click = function(tableId, editBtn, deleteBtn){
	$("#" + tableId + " tr").click(function() 
    {
        window.selectedItemId = $(this).find("a").attr("href");
		window.temp = window.selectedItemId.split("/");
		window.selectedItemId = window.temp[1];
		//alert(window.selectedItemId);
        $("#" + editBtn).attr('disabled',false);
        $("#" + deleteBtn).attr('disabled',false);
    });
}

Utils.table_tr_clickSAI = function(tableId, editBtn, deleteBtn, aprovedBtn, evaluateBtn){
  $("#" + tableId + " tr").click(function() 
    {
        window.selectedItemId = $(this).find("a").attr("href");
    window.temp = window.selectedItemId.split("/");
    window.selectedItemId = window.temp[1];
    //alert(window.selectedItemId);
        $("#" + editBtn).attr('disabled',false);
        $("#" + deleteBtn).attr('disabled',false);
        $("#" + aprovedBtn).attr('disabled',false);
        $("#" + evaluateBtn).attr('disabled',false);
    });
}

Utils.edit_click = function(editBtn, urlparam){
	$('#' + editBtn).click(function() 
    {
        //url = urlparam + " 12345".replace(/12345/, window.selectedItemId);
        //window.location = url;
        window.path = Urls.publication_edit("Files", 2);
        alert(window.path);
    });
}

/*Utils.delete_click = function(){
	$('#delete-movie').click(function() 
    {
        url = "{% url 'file_delete' 12345 %}".replace(/12345/, selectedItemId);
        window.location = url;
    });
}*/

Utils.CmbCountry_selectionChange = function(){
	$("#id_pais").change(
    function(){         
               GetMunicipalities($(this).val());
               }
   );
}

Utils.DisplayPopup = function()
{
    var appendthis =  ("<div class='modal-overlay js-modal-close'></div>");

    $('a[data-modal-id]').click(function(e) {
        e.preventDefault();
    $("body").append(appendthis);
    $(".modal-overlay").fadeTo(500, 0.7);
    //$(".js-modalbox").fadeIn(500);
        var modalBox = $(this).attr('data-modal-id');
        $('#'+modalBox).fadeIn($(this).data());
    });  
  
      
    $(".js-modal-close, .modal-overlay").click(function() {
        $(".modal-box, .modal-overlay").fadeOut(500, function() {
            $(".modal-overlay").remove();
        });
     
    });
     
    $(window).resize(function() {
        $(".modal-box").css({
            top: ($(window).height() - $(".modal-box").outerHeight()) / 2,
            left: ($(window).width() - $(".modal-box").outerWidth()) / 2
        });
    });
     
    $(window).resize();
}

Utils.Enable_DisableSearchButton = function()
{
    if ($("#id_q").val() =="") {
        $("#post-form").prop('disabled',true);    
    }else
    if ($("#id_q").val() !="")
    {
        console.log("escribiendo");
        $("#post-form").prop('disabled',false);
    }
}

Utils.testingAjax = function(valueSearch)
{
    $.ajax({
            url : "searchPub/", // the endpoint
            type : "POST", // http method
            data : { criterio : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
              $('#loading').hide();
              // Visualizamos el div que muestra los resultados de la búsqueda
              $('#searchResults').show();

              if (json_response.length == 0) {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
              }else
              {
                 // Visualizamos el div que muestra los resultados de la búsqueda
				 $('#searchResultsBody').show();
                 if (json_response.length==1) 
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
                 }else
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
                 }
                 for (var i in json_response) 
                  {
					$('#searchResultsBody').append("<a href='PublicacionView/" + json_response[i].pk + "'>" + json_response[i].fields.titulo + "</a>, del autor "+ json_response[i].fields.autor +" publicada en el año "+ json_response[i].fields.anno +"</br>");
                  }   
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
                $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}    


Utils.searchEvn = function(valueSearch)
{
    $.ajax({
            url : "searchEvn/", // the endpoint
            type : "POST", // http method
            data : { criterio : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
              $('#loading').hide();
              // Visualizamos el div que muestra los resultados de la búsqueda
              $('#searchResults').show();

              if (json_response.length == 0) {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
              }else
              {
                 // Visualizamos el div que muestra los resultados de la búsqueda
				 $('#searchResultsBody').show();
                 if (json_response.length==1) 
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
                 }else
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
                 }
                 for (var i in json_response) 
                  {
					$('#searchResultsBody').append("<a href='EventoView/" + json_response[i].pk + "'>" + json_response[i].fields.nombre + "</a>, realizado en la ciudad "+ json_response[i].fields.ciudad +" correspondiente a "+ json_response[i].fields.pais +"</br>");
                  }    
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
                $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}

Utils.searchPonEvn = function(valueSearch)
{
    $.ajax({
            url : "searchPonEvn/", // the endpoint
            type : "POST", // http method
            data : { criterio : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
              $('#loading').hide();
              // Visualizamos el div que muestra los resultados de la búsqueda
              $('#searchResults').show();

              if (json_response.length == 0) {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
              }else
              {
                 // Visualizamos el div que muestra los resultados de la búsqueda
				 $('#searchResultsBody').show();
                 if (json_response.length==1) 
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
                 }else
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
                 }
                 for (var i in json_response) 
                  {
					$('#searchResultsBody').append("<a href='PonEnvView/" + json_response[i].pk + "'>" + json_response[i].fields.titulo + "</a>, impartida por "+ json_response[i].fields.autor +" en el evento "+ json_response[i].fields.evento +"</br>");
                  }    
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
                $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}

Utils.searchCap = function(valueSearch)
{
    $.ajax({
            url : "searchCap/", // the endpoint
            type : "POST", // http method
            data : { criterio : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
              $('#loading').hide();
              // Visualizamos el div que muestra los resultados de la búsqueda
              $('#searchResults').show();

              if (json_response.length == 0) {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
              }else
              {
                 // Visualizamos el div que muestra los resultados de la búsqueda
				 $('#searchResultsBody').show();
                 if (json_response.length==1) 
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
                 }else
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
                 }
                 for (var i in json_response) 
                  {
					$('#searchResultsBody').append("<a href='CapacitacionView/" + json_response[i].pk + "'>" + json_response[i].fields.nombre + "</a>, correspondiente a la modalidad "+ json_response[i].fields.modalidad +" y al tipo "+ json_response[i].fields.tipo +"</br>");
                  }    
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
                $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}

Utils.searchPat = function(valueSearch)
{
    $.ajax({
            url : "searchPat/", // the endpoint
            type : "POST", // http method
            data : { criterio : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
              $('#loading').hide();
              // Visualizamos el div que muestra los resultados de la búsqueda
              $('#searchResults').show();

              if (json_response.length == 0) {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
              }else
              {
                 // Visualizamos el div que muestra los resultados de la búsqueda
				 $('#searchResultsBody').show();
                 if (json_response.length==1) 
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
                 }else
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
                 }
                 for (var i in json_response) 
                  {
					$('#searchResultsBody').append("<a href='PatenteView/" + json_response[i].pk + "'>" + json_response[i].fields.nombre_obra + "</a>, obtenida por "+ json_response[i].fields.propietario +" en la fecha "+ json_response[i].fields.fecha +"</br>");
                  }    
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
                $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}

Utils.searchRI = function(valueSearch)
{
    $.ajax({
            url : "searchRI/", // the endpoint
            type : "POST", // http method
            data : { criterio : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
              $('#loading').hide();
              // Visualizamos el div que muestra los resultados de la búsqueda
              $('#searchResults').show();

              if (json_response.length == 0) {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
              }else
              {
                 // Visualizamos el div que muestra los resultados de la búsqueda
				 $('#searchResultsBody').show();
                 if (json_response.length==1) 
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
                 }else
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
                 }
                 for (var i in json_response) 
                  {
					$('#searchResultsBody').append("<a href='ResultadoIntroducidoView/" + json_response[i].pk + "'>" + json_response[i].fields.nombre_obra + "</a>, obtenido por "+ json_response[i].fields.propietario +" en la fecha "+ json_response[i].fields.fecha +"</br>");
                  }   
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
                $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}

Utils.searchPre = function(valueSearch)
{
    $.ajax({
            url : "searchPre/", // the endpoint
            type : "POST", // http method
            data : { criterio : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
              $('#loading').hide();
              // Visualizamos el div que muestra los resultados de la búsqueda
              $('#searchResults').show();

              if (json_response.length == 0) {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
              }else
              {
                 // Visualizamos el div que muestra los resultados de la búsqueda
				 $('#searchResultsBody').show();
                 if (json_response.length==1) 
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
                 }else
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
                 }
                 for (var i in json_response) 
                  {
					$('#searchResultsBody').append("<a href='PremioView/" + json_response[i].pk + "'>" + json_response[i].fields.titulo + "</a>, obtenido por "+ json_response[i].fields.autor +" en el año "+ json_response[i].fields.anno +"</br>");
                  }   
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
                $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}

Utils.searchNew = function(valueSearch)
{
    $.ajax({
            url : "searchNew/", // the endpoint
            type : "POST", // http method
            data : { criterio : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
              $('#loading').hide();
              // Visualizamos el div que muestra el título de los resultados de la búsqueda
              $('#searchResults').show();
              if (json_response.length == 0) {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
              }else
              {
				 // Visualizamos el div que muestra los resultados de la búsqueda
				 $('#searchResultsBody').show();
                 if (json_response.length==1) 
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
                 }else
                 {
                    $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
                 }
                 for (var i in json_response) 
                  {
					$('#searchResultsBody').append("<a href='NoticiaView/" + json_response[i].pk + "'>" + json_response[i].fields.titular + "</a><p style='text-align:justify'>"+ json_response[i].fields.contenido +"</p></br>");
                  }   
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
                $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}

Utils.pdfSample = function(valueSearch)
{
    $.ajax({
            url : "samplePDF/", // the endpoint
            type : "GET", // http method
            data : { print : "pdf" }
        });

}

Utils.csvSample = function(valueSearch)
{
    $.ajax({
            url : "sampleCSV/", // the endpoint
        });

}

Utils.footable = function(){
  
    $('table').footable().bind('footable_filtering', function (e) {
      var selected = $('.filter-status').find(':selected').text();
      if (selected && selected.length > 0) {
        e.filter += (e.filter && e.filter.length > 0) ? ' ' + selected : selected;
        e.clear = !e.filter;
      }
    });
    $('.filter-api').click(function (e) {
      e.preventDefault();

      //get the footable filter object
      var footableFilter = $('table').data('footable-filter');

      alert('about to filter table by "tech"');
      //filter by 'tech'
      footableFilter.filter('tech');

      //clear the filter
      if (confirm('clear filter now?')) {
        footableFilter.clearFilter();
      }
    });
}
	
Utils.DisplayMessageEmptyList = function(){
  $('.bottom-left').notify({
				  message: 'Listado vacío, un reporte debe contener al menos un registro de tipo',
				  type: 'blackgloss',
				  fadeOut: {
					delay: Math.floor(Math.random() * 500) + 2500
				  }
				}).show();
}	
	
Utils.notifyWithNotifIt = function (){
            notif({
				type: "error",
				msg: "Listado vacío, para generar un reporte debe existir al menos un registro.",
				clickable: false,
				position: "center",
				width: 500,
				height: 60,
				autohide: false
			});
        }	
		
Utils.notifyInfoWithNotifIt = function (message){
            notif({
				type: "success",
				msg: message,
				clickable: false,
				position: "center",
				width: 870,
				height: 60,
				autohide: false
			});
        }	
	
})(window.Utils = window.Utils || {});
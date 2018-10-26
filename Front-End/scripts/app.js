(function() {
    'use strict';
  
    var app = {
      isLoading: true,
      visibleCards: {},
      selectedCities: [],
      spinner: document.querySelector('.loader'),
      cardTemplate: document.querySelector('.cardTemplate'),
      container: document.querySelector('.main'),
      addDialog: document.querySelector('.dialog-container'),
      daysOfWeek: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    };
  
  
    /*****************************************************************************
     *
     * Event listeners for UI elements
     *
     ****************************************************************************/
  
    function alertMsg()
    {
        alert("Message");
    }


    document.getElementById('butRefresh').addEventListener('click', function() {
      // Refresh all of the forecasts
      alertMsg();
    });
  
    document.getElementById('index_MainButton').addEventListener('click', function() {
      // Open/show the add new city dialog
      alertMsg();
    });
    // TODO add startup code here
  
    // TODO add service worker code here
  })();
  
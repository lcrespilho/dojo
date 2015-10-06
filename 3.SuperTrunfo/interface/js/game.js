(function() {

  var app = angular.module('Game', ['tabs-directive']);

  app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;
    delete $httpProvider.defaults.headers.common["X-Requested-With"];
    $httpProvider.defaults.headers.common["Accept"] = "application/json";
    $httpProvider.defaults.headers.common["Content-Type"] = "application/json";
    $httpProvider.defaults.headers.common = {};
    $httpProvider.defaults.headers.post = {};
    $httpProvider.defaults.headers.put = {};
    $httpProvider.defaults.headers.patch = {};
    }
  ]);

  app.directive('mainTab', function(){
    return {
      restrict: 'E',
      templateUrl: 'views/main-tab.html',
      controller:function(){
        this.tab = 1;
        this.isSet = function(checkTab) {
          return this.tab === checkTab;
        };
        this.setTab = function(setTab) {
          this.tab = setTab;
        };
      },
      controllerAs:'tab'
    };
  });

  app.controller('gameController', ['$http', function($http){
    var controller = this;
    controller.session = '';

    this.createSession = function(deck) {
      var temp_values = this;
      temp_values.cards = [];
      temp_values.attributes = deck.attributes;


      $http({
        method: 'GET',
        url: 'http://localhost\:5000/dojo/decks/'+deck.name+'/cards'
        }).success(function(data){
          temp_values.cards = data;

          data_json = {
            'action': 'create_session',
            'deck_cards': temp_values.cards,
            'attributes': temp_values.attributes
          }
          data_json = JSON.stringify(data_json);
          console.log(data_json);

          $http({
            method: 'POST',
            url: 'http://localhost\:8891',
            data: JSON.stringify(data_json),
            // headers: {'Content-Type': 'application/json'}
          }).success(function(data){
              console.log('sucesso222');
              controller.session = data;
              console.log('bbbT' + controller.session)
          });
      });

    };

  }]);

})();

// data: JSON.stringify({
//   'action': 'create_session',
//   'deck_cards': temp_values.cards,
//   'attributes': temp_values.attributes
// }),

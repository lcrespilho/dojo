(function(){

  var app = angular.module('tabs-directive', []);

  app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.withCredentials = true;
    delete $httpProvider.defaults.headers.common["X-Requested-With"];
    $httpProvider.defaults.headers.common["Accept"] = "application/json";
    $httpProvider.defaults.headers.common["Content-Type"] = "application/json";
    }
  ]);

  app.controller('DecksController', ['$http', function($http){
    var controller = this;
    controller.decks = [];
    controller.session = '';

    $http({
      method: 'GET',
      url: 'http://localhost\:5000/dojo/decks'
      }).success(function(data){
        controller.decks = data;
    });

  }]);

  app.directive('newGame', function(){
    return {
      restrict: 'E',
      templateUrl: 'views/new-game.html',
    };
  });

  app.directive('rooms', function(){
    return {
      restrict: 'E',
      templateUrl: 'views/rooms.html'
    };
  });

  app.directive('randomGame', function(){
    return {
      restrict: 'E',
      templateUrl: 'views/random-game.html'
    };
  });

  app.directive('rules', function(){
    return {
      restrict: 'E',
      templateUrl: 'views/rules.html'
    };
  });

})();

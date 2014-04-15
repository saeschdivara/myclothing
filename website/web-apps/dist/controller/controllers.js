(function() {
  window.clothingApp = angular.module('clothing-app', ['ngCookies']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    return $interpolateProvider.endSymbol('$}');
  }).run(function($http, $cookies) {
    $http.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $http.defaults.xsrfCookieName = 'csrftoken';
    return $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  });

  window.myServices = angular.module('myServices', ['ngResource']);

  clothingApp.factory('clothingTimeManager', [
    '$http', '$q', function($http, $q) {
      var clothingTimeManager;
      return clothingTimeManager = {
        test: 2,
        loadAll: function() {
          var deferred;
          deferred = $q.defer();
          $http.get('/api/users').success(function(list) {
            console.log(list);
            return deferred.resolve(list);
          }).error(function() {
            return deferred.reject();
          });
          return deferred.promise;
        }
      };
    }
  ]);

  clothingApp.controller('ClothingTimeController', [
    '$scope', 'clothingTimeManager', function($scope, clothingTimeManager) {
      return clothingTimeManager.loadAll().then((function(_this) {
        return function(userList) {
          return $scope.users = userList;
        };
      })(this));
    }
  ]);

}).call(this);

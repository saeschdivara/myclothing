(function () {
  window.clothingApp = angular.module('clothing-app', ['ngCookies']).config([
    '$interpolateProvider',
    function ($interpolateProvider) {
      $interpolateProvider.startSymbol('{$');
      return $interpolateProvider.endSymbol('$}');
    }
  ]).run([
    '$http',
    '$cookies',
    function ($http, $cookies) {
      $http.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
      $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
      $http.defaults.xsrfCookieName = 'csrftoken';
      return $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
  ]);
  window.myServices = angular.module('myServices', ['ngResource']);
  clothingApp.factory('clothingTimeManager', [
    '$http',
    '$q',
    'ClothingTimeFactory',
    function ($http, $q, ClothingTimeFactory) {
      var clothingTimeManager;
      clothingTimeManager = {
        test: 2,
        loadAll: function () {
          var deferred;
          deferred = $q.defer();
          $http.get('/api/clothing-time/').success(function (list) {
            var clothingTime, time, times, _i, _len;
            times = [];
            for (_i = 0, _len = list.length; _i < _len; _i++) {
              clothingTime = list[_i];
              time = ClothingTimeFactory.$new();
              time.setData(clothingTime);
              times.push(time);
            }
            console.log(times);
            return deferred.resolve(times);
          }).error(function () {
            return deferred.reject();
          });
          return deferred.promise;
        }
      };
      return clothingTimeManager;
    }
  ]);
  clothingApp.controller('ClothingTimeController', [
    '$scope',
    'clothingTimeManager',
    function ($scope, clothingTimeManager) {
      return clothingTimeManager.loadAll().then(function (_this) {
        return function (clothingtimeList) {
          return $scope.clothingtimes = clothingtimeList;
        };
      }(this));
    }
  ]);
}.call(this));
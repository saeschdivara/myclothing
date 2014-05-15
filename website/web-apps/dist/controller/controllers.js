(function() {
  var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  window.clothingApp = angular.module('clothing-app', ['ngCookies', 'ngResource']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    return $interpolateProvider.endSymbol('$}');
  }).run(function($http, $cookies) {
    $http.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $http.defaults.xsrfCookieName = 'csrftoken';
    return $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  });

  clothingApp.controller('BodyController', [
    '$scope', 'BodyPartResource', function($scope, BodyPartResource) {
      var $controller, BodyController;
      BodyController = (function() {
        function BodyController() {
          this.$onClothingChosen = __bind(this.$onClothingChosen, this);
          this.head = '';
          this.upper_body_part = '';
          this.lower_body_part = '';
          this.left_arm = '';
          this.right_arm = '';
          this.left_foot = '';
          this.right_foot = '';
          this.all_parts = BodyPartResource.get();
          console.log(this.all_parts);
        }

        BodyController.prototype.$onClothingChosen = function(event, message) {
          return console.log(event);
        };

        return BodyController;

      })();
      $scope.foo = 'dddd';
      $controller = new BodyController();
      $scope.$on('CLOTHING_IS_CHOSEN', $controller.$onClothingChosen);
      return $controller;
    }
  ]);

  clothingApp.factory('clothingTimeManager', [
    '$http', '$q', 'ClothingTimeFactory', function($http, $q, ClothingTimeFactory) {
      var clothingTimeManager;
      clothingTimeManager = {
        test: 2,
        loadAll: function() {
          var deferred;
          deferred = $q.defer();
          $http.get('/api/clothing-time/').success(function(list) {
            var clothingTime, time, times, _i, _len;
            times = [];
            for (_i = 0, _len = list.length; _i < _len; _i++) {
              clothingTime = list[_i];
              time = ClothingTimeFactory.$new();
              time.setData(clothingTime);
              times.push(time);
            }
            return deferred.resolve(times);
          }).error(function() {
            return deferred.reject();
          });
          return deferred.promise;
        }
      };
      return clothingTimeManager;
    }
  ]);

  clothingApp.controller('ClothingTimeController', [
    '$scope', '$rootScope', 'clothingTimeManager', function($scope, $rootScope, clothingTimeManager) {
      var $controller, ClothingTimeController;
      clothingTimeManager.loadAll().then((function(_this) {
        return function(clothingtimeList) {
          return $scope.clothingtimes = clothingtimeList;
        };
      })(this));
      ClothingTimeController = (function() {
        function ClothingTimeController() {

          /*
           */
        }

        ClothingTimeController.prototype.$onClothingChosen = function(clothing) {

          /*
           */
          return $rootScope.$broadcast('CLOTHING_IS_CHOSEN', {
            clothing: clothing
          });
        };

        return ClothingTimeController;

      })();
      $controller = new ClothingTimeController();
      $scope.onClothingChosen = $controller.$onClothingChosen;
      return $controller;
    }
  ]);

}).call(this);

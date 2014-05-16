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
    '$scope', '$timeout', 'BodyPartResource', function($scope, $timeout, BodyPartResource) {
      var $controller, BodyController;
      BodyController = (function() {
        function BodyController() {
          this.$onClothingChosen = __bind(this.$onClothingChosen, this);
          this.body_data = {
            head: '',
            upper_body_part: '',
            lower_body_part: '',
            left_arm: '',
            right_arm: '',
            left_leg: '',
            right_leg: ''
          };
          BodyPartResource.query().$promise.then((function(_this) {
            return function(result) {
              return _this.all_parts = result;
            };
          })(this));
        }

        BodyController.prototype.$onClothingChosen = function(event, message) {
          var body_part_id, body_part_name, body_part_object, clothing, part, _i, _len, _ref;
          clothing = message.clothing;
          body_part_id = clothing.body_parts[0];
          body_part_object = null;
          _ref = this.all_parts;
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            part = _ref[_i];
            if (part.id === body_part_id) {
              body_part_object = part;
              break;
            }
          }
          if (part) {
            body_part_name = part.name.toLowerCase().replace(/[ ]/, '_');
            return $timeout((function(_this) {
              return function() {
                _this.body_data[body_part_name] = clothing.image;
                return $scope.$apply();
              };
            })(this));
          }
        };

        return BodyController;

      })();
      $controller = new BodyController();
      $scope.$on('CLOTHING_IS_CHOSEN', $controller.$onClothingChosen);
      $scope.foo = 'dddd';
      $scope.bodyData = $controller.body_data;
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

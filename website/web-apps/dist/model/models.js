(function() {
  clothingApp.factory('ClothingResource', [
    '$resource', function($resource) {
      return $resource('/api/clothing/:id/', {
        id: '@id'
      }, {
        stripTrailingSlashes: false
      });
    }
  ]);

  clothingApp.factory('ClothingTimeFactory', [
    'ClothingResource', function(ClothingResource) {
      var ClothingTime, ClothingTimeFactory;
      ClothingTime = (function() {
        function ClothingTime(isVisible) {
          this.isVisible = isVisible != null ? isVisible : false;
        }

        ClothingTime.prototype.setData = function(obj) {
          var clothing_id, clothing_obj, _i, _len, _ref, _results;
          this.name = obj.name;
          this.slug = obj.slug;
          this.image = obj.image;
          this.clothes = [];
          _ref = obj.clothes;
          _results = [];
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            clothing_id = _ref[_i];
            clothing_obj = ClothingResource.get({
              id: clothing_id
            });
            _results.push(clothing_obj.$promise.then((function(_this) {
              return function(data) {
                return _this.clothes.push(data);
              };
            })(this)));
          }
          return _results;
        };

        ClothingTime.prototype.setVisible = function(isVisible) {
          return this.isVisible = isVisible;
        };

        return ClothingTime;

      })();
      return ClothingTimeFactory = {
        $new: function() {
          return new ClothingTime();
        }
      };
    }
  ]);

}).call(this);

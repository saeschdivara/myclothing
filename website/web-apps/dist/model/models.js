(function() {
  clothingApp.factory('ClothingResource', [
    '$resource', function($resource) {
      return $resource('http://0.0.0.0:9222/api/clothing/:id', {
        id: '@id'
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
          var clothe_obj, clothe_url, _i, _len, _ref, _results;
          this.name = obj.name;
          this.slug = obj.slug;
          this.image = obj.image;
          this.clothes = [];
          _ref = obj.clothes;
          _results = [];
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            clothe_url = _ref[_i];
            clothe_obj = ClothingResource.get(clothe_url);
            _results.push(clothe_obj.$promise.then((function(_this) {
              return function(data) {
                console.log(data);
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

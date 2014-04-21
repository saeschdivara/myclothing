(function() {
  clothingApp.factory('ClothingTimeFactory', [
    function() {
      var ClothingTime, ClothingTimeFactory;
      ClothingTime = (function() {
        function ClothingTime(isVisible) {
          this.isVisible = isVisible != null ? isVisible : false;
        }

        ClothingTime.prototype.setData = function(obj) {
          this.name = obj.name;
          this.slug = obj.slug;
          return this.image = obj.image;
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

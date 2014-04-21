clothingApp.factory('ClothingTimeFactory', [() ->
    class ClothingTime

      constructor: (@isVisible = false) ->

      setData: (obj) ->
        @name = obj.name
        @slug = obj.slug
        @image = obj.image

      setVisible: (isVisible) ->
        @isVisible = isVisible

    ClothingTimeFactory =
      $new: () ->
        return new ClothingTime()
])
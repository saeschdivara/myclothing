clothingApp.factory('ClothingTimeFactory', [() ->
    class ClothingTime

      constructor: (@isVisible = false) ->

      setData: (obj) ->
        @name = obj.name
        @slug = obj.slug

      setVisible: (isVisible) ->
        @isVisible = isVisible

    ClothingTimeFactory =
      $new: () ->
        return new ClothingTime()
])
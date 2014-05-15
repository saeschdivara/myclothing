clothingApp.factory('BodyPartResource', [ '$resource', ($resource) ->
    return $resource('/api/body/:id/',
        id: '@id'
    ,
        stripTrailingSlashes: false
    )
])
mainApp.factory("Item", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/items/:id/", {id: '@id'}, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("Type", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/types/:id/", {id: '@id'}, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("Location", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/locations/:id/", {id: '@id'}, {
            'update': {method: 'PUT'}
        });
    }]);

mainApp.factory("Attribute", ['$resource',
    function ($resource) {
        return $resource("http://localhost:5000/api/v1/types/:typeid/attributes/:attributeid", {
            typeid: '@typeid',
            attributeid: '@attributeid'
        }, {
            'update': {method: 'PUT'}
        });
    }]);

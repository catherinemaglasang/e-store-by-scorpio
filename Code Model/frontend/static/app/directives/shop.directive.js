
mainApp.directive("singleProduct", function(){
	return {
		restrict: 'E',
		templateUrl: "static/partials/single-product.html"
	};
});

mainApp.directive("cartItem", function(){
	return {
		restrict: 'E',
		templateUrl: "static/partials/cart-item.html"
	};
});

mainApp.directive("owlCarousel", function(){
	return {
		restrict: 'A',
		link: function(scope, element, attrs){
			$(element).owlCarousel(scope.$eval(attrs.owlCarousel));
		}
	}
});

mainApp.directive("priceSlider", function(){
	return {
		restrict: 'A',
		link: function(scope, element, attrs){
			$(element).ionRangeSlider(scope.$eval(attrs.priceSlider));
		}
	}
});

mainApp.directive("iCheck", function(){
	return {
		restrict: 'A',
		link: function(scope, element, attrs){
			$(element).iCheck({
				checkboxClass: 'i-check',
				radioClass: 'i-radio'
			});
		}
	}
})
var app = angular.module("departments",['common_module','ui.router','ui.calendar']);

app.controller('departmentsCtrl', function($scope,$http,$controller,$state,CommonFunc,CommonRead,CommonFac){
    angular.extend(this, $controller('CommonCtrl', {$scope: $scope}));
    var me = this;


    me.read_pagination = function(){
    	
    }




});
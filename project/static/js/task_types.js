var app = angular.module("task_types",['common_module','ui.router','ui.calendar']);

app.controller('task_typesCtrl', function($scope,$http,$controller,$state,CommonFunc,CommonRead,CommonFac){
    angular.extend(this, $controller('CommonCtrl', {$scope: $scope}));
    var me = this;
    me.IsVisible = false;
    me.isVisible2 = false;


    me.delete = function(record){
        var confirmation = CommonFunc.confirmation("Continue delete?");
        console.log(record)
        confirmation.then(function(){
            var post = me.post_generic("/task_types/delete_task/",record,"main",true)
            post.success(function(response){
                me.read_pagination();
            })
        })
    }

    // me.edit = function(record){
    //     console.log(record)
    //     var post = me.post_generic("/task_types/edit_task/",record,true)
    //     post.success(function(response){
    //             current_record = response.data;
    //             console.log(response.data)
    //             console.log(me.records[0].id)
    //     })

        
    // }
    me.read_pagination = function(record){
        var filters = angular.copy(me.filters)
    	var post = me.post_generic("/task_types/read_pagination/",filters,"main")
        post.success(function(response){
			console.log(response.data)
            me.records = response.data;
            me.generate_pagination(me,response);

        }); 
        	
    	
    }
    me.create = function(record){
        console.log(me.record)
        var post = me.post_generic("/task_types/create/",me.record,"main",true,false,true)
        post.success(function(response){
            me.read_pagination();


        })
    }
    me.create_dialog = function(current_record){
        me.record={}

        if (current_record){
            me.record =  angular.copy(current_record)
        }
        
        me.open_dialog("/task_types/create_dialog/","dialog_height_100 dialog_width_70");
    }

    me.read_pagination();




});
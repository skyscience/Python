$(function(){

    $.get('area1/',function(dic) {
    pro=$('#pro')
    $.each(dic.data,function(index,item){
    pro.append('<option value='+item[0]+'>'+item[1]+'</option>');
    })
    });
    
    $('#pro').change(function(){
    $.post($(this).val()+'/',function(dic){
    city=$('#city');
    city.empty().append('<option value="">请选择市</option>');
    $.each(dic.data,function(index,item){
    city.append('<option value='+item.id+'>'+item.title+'</option>');
    })
    });
    });
    
    $('#city').change(function(){
    $.post($(this).val()+'/',function(dic){
    dis=$('#dis');
    dis.empty().append('<option value="">请选择区县</option>');
    $.each(dic.data,function(index,item){
    dis.append('<option value='+item.id+'>'+item.title+'</option>');
    })
    })
    });
    
    });
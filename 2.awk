BEGIN{
    temp = $1;
    var["name"] = 0;
    var["ip"] = 0;
}
{   
    name = temp;
    temp = $1;
    ip = $2;
    if( ip ~ /[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/ ){
        var["name"] = substr(name,0,length(name)-1);
        var["ip"] = ip;
        print "name:",var["name"],"ip:",var["ip"];
    }
}

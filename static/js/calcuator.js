let result=document.getElementById('screen');
       let str="";
        fun=(arr)=> {
            if(arr=='=')
            {
                result.value=eval(result.value);
            }
            else if(arr=='AC')
            {
                result.value="";
            }
            else if(arr=='C')
            {
                result.value=result.value.substring(0,result.value.length-1);
            }
            else if(arr=='^')
            {
                str="**";
                result.value+=str;
            }
            else
            {
            result.value +=arr;
            }
            result.innerHTML=result.value;
            
        }
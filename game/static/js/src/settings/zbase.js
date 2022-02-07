class Settings{
    constructor(root) {
        this.root = root;
        this.platform = "WEB";
        if(this.root.AcWingOS) this.platform = "ACAPP";
        this.username = "";
        this.p = "";
        this.k = "cccccccccccc";

        this.start();
    }

    start(){
        this.getinfo();
    }

    register(){

    }

    login(){   //打开登录界面

    }

    getinfo(){
        console.log(555)
        let outer = this;
        $.ajax({
            url: "https://app1432.acapp.acwing.com.cn/settings/getinfo/",
            type: "GET",
            data: {
                platform: outer.platform,
            },
            success: function (resp){
                console.log(resp);
                if(resp.result === "success"){
                    outer.username = resp.username;
                    outer.photo = resp.photo;
                    outer.hide();
                    outer.root.menu.show();
                    console.log(resp);
                }else{
                    outer.login();
                }
            }
        })
    }

    hide(){

    }

    show(){

    }


}
class AcGameMenu{
    constructor(root) {
        this.root = root;
        this.$menu = $(`
<div class="ac-game-menu">
    <div class="ac-game-menu-field">
        <div class="ac-game-menu-field-item ac-game-menu-field-single-mode" >
            单机模式
        </div>
        <br>
        <div class="ac-game-menu-field-item ac-game-menu-field-multi-mode">
            联机模式
        </div>
        <br>
        <div class="ac-game-menu-field-item ac-game-settings-field-illustrate">
            游戏说明
        </div>
        <br>
        <div class="ac-game-menu-field-item ac-game-menu-field-settings">
            退出登录
        </div>
    </div>
<div class="ac-game-menu-field-detail" style="text-indent:2em;">
    Moba类射击对战游戏，鼠标右键移动，Q为射击技能，F为闪现技能。匹配联机需要三人。右下角显示技能冷却时间。
</div>    
    
</div>

        `);
        this.$menu.hide();
        this.root.$ac_game.append(this.$menu);
        this.$single = this.$menu.find(".ac-game-menu-field-single-mode");
        this.$multi = this.$menu.find(".ac-game-menu-field-multi-mode");
        this.$settings = this.$menu.find(".ac-game-menu-field-settings");
        this.$illustrate = this.$menu.find(".ac-game-settings-field-illustrate")
        this.$detail = this.$menu.find(".ac-game-menu-field-detail");

        this.$detail.hide();
        this.start();
    }

    start(){
        this.add_listening_event();
    }

    add_listening_event(){
        let outer = this
        this.$single.click(function (){
            outer.hide();
            outer.root.playground.show("single mode");
        })
        this.$multi.click(function (){
            outer.hide();
            outer.root.playground.show("multi mode");
        })
        this.$settings.click(function (){
            outer.root.settings.logout_on_remote();
        })
        this.$illustrate.click(function (){
            if($(".ac-game-menu-field-detail").css("display")==='none'){
                outer.$detail.show();    //如果元素为隐藏,则将它显现
            }else{
                outer.$detail.hide();     //如果元素为显现,则将其隐藏
            }
        })
    }

    show(){  //显示menu
        this.$menu.show();
    }

    hide(){  //关闭menu
        this.$menu.hide();
    }
}

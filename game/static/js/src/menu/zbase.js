class AcGameMenu{
    constructor(root) {
        console.log(2222)
        this.root = root;
        this.$menu = $(`
<div class="ac-game-menu">
    <div class="ac-game-menu-field">
        <div class="ac-game-menu-field-item ac-game-menu-field-single-mode" >
            单人模式
        </div>
        <br>
        <div class="ac-game-menu-field-item ac-game-menu-field-multi-mode">
            多人模式
        </div>
        <br>
        <div class="ac-game-menu-field-item ac-game-menu-field-settings">
            设置
        </div>
    </div>
</div>
        `);
        console.log(3333)
        this.root.$ac_game.append(this.$menu);
        this.$single = this.$menu.find(".ac-game-menu-field-single-mode");
        this.$multi = this.$menu.find(".ac-game-menu-field-multi-mode");
        this.$settings = this.$menu.find(".ac-game-menu-field-settings");

        this.start();
    }

    start(){
        this.add_listening_event();
    }

    add_listening_event(){
        let outer = this
        this.$single.click(function (){
            outer.hide();
            outer.root.playground.show();
            // console.log("click single mod")
        })
        this.$multi.click(function (){
            console.log("click multi mode")
        })
        this.$settings.click(function (){
            console.log("click settings")
        })
    }

    show(){  //显示menu
        this.$menu.show();
    }

    hide(){  //关闭menu
        this.$menu.hide();
    }
}

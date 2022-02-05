class AcGameMenu{
    constructor(root) {
        console.log(2222)
        this.root = root;
        this.$menu = $(`
<div class="ac-game-menu">
    <div class="ac-game-menu-field">
        <div class="ac-game-menu-field-item ac-game-menu-field-single" >
            单人模式
        </div>
        <br>
        <div class="ac-game-menu-field-item ac-game-menu-field-multi">
            多人模式
        </div>
        <br>
        <div class="ac-game-menu-field-item ac-game-menu-field-item-settings">
            设置
        </div>
    </div>
</div>
        `);
        console.log(3333)
        this.root.$ac_game.append(this.$menu);
        this.$single = this.$menu.find(".ac-game-menu-field-single");
        this.$multi = this.$menu.find(". ac-game-menu-field-multi");
        this.$settings = this.$menu.find(". ac-game-menu-field-settings");
    }
}

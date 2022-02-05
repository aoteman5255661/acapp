class AcGameMenu{
    constructor(root) {
        console.log(2222)
        this.root = root;
        this.$menu = $(`
<div class="ac-game-menu">
</div>
        `);
        console.log(3333)
        this.root.$ac_game.append(this.$menu);
        console.log(4444)
    }
}

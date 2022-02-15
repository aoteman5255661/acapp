export class AcGame {
    constructor(id, AcWingOS) {
        this.id = id;
        this.$ac_game = $('#' + id);
        this.AcWingOS = AcWingOS;

        // this.bgmplay = this.bgm.find('.ac-game-settings-bgm')
        // console.log(this.bgmplay)
        // this.bgmplay.hide()
        this.$ac_game.append(this.bgm)

        // this.bgm.show();
        this.settings = new Settings(this);
        this.menu = new AcGameMenu(this);

        this.playground = new AcGamePlayground(this);

        this.start();
    }

    start(){

    }
}

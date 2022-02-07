export class AcGame{
    constructor(id, AcWingOS) {
        console.log(111)
        this.id=id;
        this.$ac_game = $('#' + id);
        this.AcWingOS = AcWingOS;
        console.log('kkkk')
        this.settings = new Settings(this);

        console.log('uuuuu')
        this.menu = new AcGameMenu(this);
        this.playground = new AcGamePlayground(this);

        this.start();
    }

    start(){

    }
}

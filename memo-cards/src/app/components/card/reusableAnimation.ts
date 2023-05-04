import { animation , style, animate} from "@angular/animations";

export const reusableAnimation = animation([
    style({
        opacity: '{{ opacity }}' || 0,
        backgroundImage: '{{ backgroundImage }}' || 'none'
    }),
    animate('{{ time }} {{ animateFucntion }}')
])
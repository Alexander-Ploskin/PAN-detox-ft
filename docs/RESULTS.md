# Результаты

### Baseline Duplicate

Конфиг : —

Run W&B : —

Краткое описание : Вход подается на выход

Результаты:

| Language           | STA   | SIM   | CHRF  | J     | XCOMET |
| ------------------ | ----- | ----- | ----- | ----- | ------ |
| am                 | 0.730 | 0.810 | 0.486 | 0.461 | 0.760  |
| ar                 | 0.680 | 0.926 | 0.776 | 0.564 | 0.890  |
| de                 | 0.630 | 0.946 | 0.812 | 0.572 | 0.959  |
| en                 | 0.533 | 0.892 | 0.670 | 0.353 | 0.739  |
| es                 | 0.700 | 0.887 | 0.655 | 0.566 | 0.902  |
| fr                 | 0.522 | 0.947 | 0.827 | 0.458 | 0.926  |
| he                 | 0.570 | 0.827 | 0.544 | 0.405 | 0.841  |
| hi                 | 0.539 | 0.889 | 0.695 | 0.417 | 0.865  |
| hin                | 0.596 | 0.885 | 0.682 | 0.418 | 0.778  |
| it                 | 0.745 | 0.963 | 0.810 | 0.656 | 0.912  |
| ja                 | 0.524 | 0.946 | 0.763 | 0.438 | 0.884  |
| ru                 | 0.525 | 0.895 | 0.699 | 0.424 | 0.899  |
| tt                 | 0.734 | 0.929 | 0.784 | 0.587 | 0.855  |
| uk                 | 0.516 | 0.940 | 0.778 | 0.442 | 0.910  |
| zh                 | 0.630 | 0.874 | 0.536 | 0.477 | 0.857  |
| Average_p J        | -     | -     | -     | 0.475 | -      |
| Average_np J       | -     | -     | -     | 0.493 | -      |
| Average all XCOMET | -     | -     | -     | 0.865 | -      |

### Baseline Delete

Конфиг : —

Run W&B : —

Краткое описание : С помощью словаря вырезаются все токсиные слова

Результаты:

| Language           | STA   | SIM   | CHRF  | J     | XCOMET |
| ------------------ | ----- | ----- | ----- | ----- | ------ |
| am                 | 0.750 | 0.808 | 0.487 | 0.461 | 0.739  |
| ar                 | 0.788 | 0.916 | 0.778 | 0.611 | 0.842  |
| de                 | 0.657 | 0.941 | 0.803 | 0.586 | 0.949  |
| en                 | 0.826 | 0.882 | 0.689 | 0.473 | 0.663  |
| es                 | 0.795 | 0.878 | 0.662 | 0.603 | 0.854  |
| fr                 | 0.647 | 0.948 | 0.832 | 0.524 | 0.863  |
| he                 | 0.659 | 0.823 | 0.548 | 0.445 | 0.777  |
| hi                 | 0.630 | 0.886 | 0.706 | 0.480 | 0.848  |
| hin                | 0.622 | 0.878 | 0.676 | 0.421 | 0.753  |
| it                 | 0.854 | 0.948 | 0.796 | 0.676 | 0.834  |
| ja                 | 0.524 | 0.946 | 0.763 | 0.438 | 0.884  |
| ru                 | 0.663 | 0.889 | 0.709 | 0.514 | 0.869  |
| tt                 | 0.775 | 0.926 | 0.790 | 0.611 | 0.843  |
| uk                 | 0.707 | 0.932 | 0.792 | 0.581 | 0.884  |
| zh                 | 0.831 | 0.818 | 0.525 | 0.516 | 0.748  |
| Average_p J        | -     | -     | -     | 0.536 | -      |
| Average_np J       | -     | -     | -     | 0.519 | -      |
| Average all XCOMET | -     | -     | -     | 0.823 | -      |

### Файнтюн mT5 на Paradetox

Конфиг : TODO

Run W&B : [Weights & Biases](https://wandb.ai/kozlovskij-vu/huggingface?nw=nwuserkozlovskijvu)

Краткое описание : Файнтюн втупую на парном датасете

Результаты:

| Language           | STA   | SIM   | CHRF  | J     | XCOMET |
| ------------------ | ----- | ----- | ----- | ----- | ------ |
| am                 | 0.842 | 0.623 | 0.292 | 0.309 | 0.562  |
| ar                 | 0.781 | 0.667 | 0.588 | 0.328 | 0.605  |
| de                 | 0.813 | 0.837 | 0.618 | 0.587 | 0.853  |
| en                 | 0.881 | 0.844 | 0.688 | 0.598 | 0.791  |
| es                 | 0.805 | 0.824 | 0.611 | 0.557 | 0.819  |
| fr                 | 0.630 | 0.814 | 0.637 | 0.408 | 0.763  |
| he                 | 0.724 | 0.674 | 0.380 | 0.326 | 0.631  |
| hi                 | 0.719 | 0.822 | 0.649 | 0.487 | 0.786  |
| hin                | 0.636 | 0.749 | 0.528 | 0.315 | 0.628  |
| it                 | 0.788 | 0.819 | 0.590 | 0.509 | 0.758  |
| ja                 | 0.542 | 0.887 | 0.628 | 0.385 | 0.786  |
| ru                 | 0.851 | 0.833 | 0.648 | 0.597 | 0.824  |
| tt                 | 0.692 | 0.783 | 0.604 | 0.419 | 0.741  |
| uk                 | 0.841 | 0.851 | 0.679 | 0.601 | 0.820  |
| zh                 | 0.733 | 0.780 | 0.434 | 0.448 | 0.772  |
| Average_p          | -     | -     | -     | 0.501 | -      |
| Average_np J       | -     | -     | -     | 0.394 | -      |
| Average all XCOMET | -     | -     | -     | 0.743 | -      |

Анализ:
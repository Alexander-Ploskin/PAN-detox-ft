# SVATS at PAN 2025 TextDetox: Multilingual Text Detoxification

A comprehensive solution for multilingual text detoxification achieving competitive performance with small-to-medium scale models (1-8B parameters) across 15 languages.

## Overview

This repository contains our submission to the PAN 2025 Multilingual Text Detoxification Task. Our approach demonstrates that smaller, efficiently trained models can outperform larger baselines while maintaining computational efficiency. We achieved competitive results across multiple languages using strategic model selection, synthetic data generation, and parameter-efficient fine-tuning techniques.

## Key Results

- **Outperformed 13B baseline** with models ranging from 1B to 8B parameters
- **Language-specific optimization** yielding superior performance compared to universal approaches
- **Exceeded baseline performance** in several languages including Spanish, French, Italian, and Hebrew
- **Efficient training** using LoRA adaptation and synthetic data augmentation

## Methodology

### Model Architectures
- **Qwen2-7B**: Optimal for Slavic languages (Russian, Ukrainian) and German
- **Gemma-2 4B**: Superior performance in Romance languages with compiled datasets
- **T5/mT5**: Encoder-decoder baseline with multilingual capabilities

### Training Strategies
- **Parameter-efficient fine-tuning** using LoRA adaptation
- **Synthetic data generation** to address data scarcity in low-resource languages
- **Language-specific model selection** based on J-score optimization
- **Multi-stage data filtering** based on toxicity, fluency, and similarity metrics

### Data Sources
- [ParaDetox dataset (official training data)](https://huggingface.co/datasets/textdetox/multilingual_paradetox)
- [mT0 dataset from previous year's winners](https://github.com/bigscience-workshop/xmtf?tab=readme-ov-file#data)
- [SynthDetoxM dataset](https://huggingface.co/datasets/s-nlp/synthdetoxm)
- Custom synthetic data generated using multi-stage pipeline
- Filtered dataset of ~40k toxic-neutral sentence pairs

## Key Findings

### Ablation Studies
- **LoRA effectiveness**: Comparable performance to full fine-tuning with significantly reduced computational requirements
- **Training duration**: Optimal results around 2000 steps, with overfitting beyond 2468 steps for English-only training
- **Data filtration**: Quality-based filtering consistently improves performance across languages

### Language-Specific Insights
- **High-resource languages**: Qwen2-7B with multilingual prompting achieved strongest performance
- **Romance languages**: Gemma-2 4B with compiled datasets consistently outperformed alternatives
- **Low-resource languages**: Challenging performance, highlighting need for better cross-lingual transfer

## Citation

If you use this code or approach in your research, please cite our PAN 2025 paper:

```bibtex
@inproceedings{kozlovskiy2025svats,
  title={SVATS at PAN 2025 TextDetox: Can Small Models Outperform Large Ones in Text Detoxification?},
  author={Kozlovskiy, Vladislav and Ploskin, Alexander and Tantry, Sameer and Matveeva, Tatyana and Savelyeva, Sofya},
  booktitle={CLEF 2025},
  year={2025}
}
```

## Team

**SVATS Team** - Skolkovo Institute of Science and Technology
- [Vladislav Kozlovskiy](https://github.com/VladKozlovskiy)
- [Sameer Tantry](https://github.com/sameertantry)
- [Alexander Ploskin](https://github.com/Alexander-Ploskin)
- [Tatyana Matveeva](https://github.com/tnmtvv)
- [Sofya Savelyeva](https://github.com/sofyafyaa)

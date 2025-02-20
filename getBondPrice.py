{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/YexiaoyuQing/hw1/blob/main/getBondPrice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SMC-bUUN9-gj",
        "outputId": "ea29bdff-95f9-4a48-ae96-2c3f3919a81e"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2170604.056735517"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ],
      "source": [
        "#!/usr/bin/env python3\n",
        "# -*- coding: utf-8 -*-\n",
        "\"\"\"\n",
        "Created on Tue Jun 11 21:18:56 2024\n",
        "\n",
        "@author: tleitch\n",
        "\"\"\"\n",
        "\n",
        "def getBondPrice(y, face, couponRate, m, ppy=1):\n",
        "    #df=1/(1+y/ppy) #\"discount factor\"\n",
        "    couponRate_effective = couponRate/ppy\n",
        "    coupon = couponRate_effective*face\n",
        "    time_effective = m*ppy\n",
        "    interest_rate = y/ppy\n",
        "    bondPrice = coupon*(1-(1/(1+interest_rate)**time_effective))/interest_rate + face/(1+interest_rate)**time_effective\n",
        "    return(bondPrice)\n",
        "\n",
        "\n",
        "# Test values\n",
        "\n",
        "y = 0.03\n",
        "face = 2000000\n",
        "couponRate = 0.04\n",
        "m = 10\n",
        "ppy = 1\n",
        "ppy = 2\n",
        "#<no ppy value passed>\n",
        "\n",
        "getBondPrice(y, face, couponRate, m)"
      ]
    }
  ]
}
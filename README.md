# Garden timeseries

Data has been manually gathered with a timelapse of 30s. There are missing readings of sensors and ground moisture sensor brokes after X time, so some preprocessing is needed.

@TODO : photos and schema of sensor on plant

## How to execute

### Requirements

- ydata_profiling
- pandas
- numpy
- matplotlib
- statsmodels

Create the following folder tree for data:

```txt
|
|- data
 |
 |- processed
 |- split
```

## Notebooks

- `EDA.ipynb` generates a description on data.
- `preprocessing.ipynb` generates a new csv to train the model.

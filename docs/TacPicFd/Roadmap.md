### TacPicFd

Tactical Picture Federate (TacPicFd) — see its [release notes](TacPicFd/ReleaseNotes.md).

#### Elevation data formats

1. USGS DEM (www.usgs.gov)
2. NIMA DTED
3. USGS GTOPO30
4. SDTS DEM in raster form

#### Implementation technology

- Visual C# + WPF + XNA (or Bing Maps)

#### Main functions

1. **Advanced Tactical Display** — zooming, scrolling, displaying the area/chart, displaying the contacts, etc.
2. **Message Center** — sending and receiving tactical messages, etc.
3. **Pinning** — measuring distances and bearings on the chart, rulers, etc.
4. **Commanding the Surface Task Group and formation** — grouping/ungrouping ships, ordering the STG course/speed/formation type.

#### Design note

- One option is to use a library that converts vector maps into images and do everything on images. The trade-off: the resulting tactical picture tool could not meet some analysis needs.
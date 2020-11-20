require(tools)

rm(list = ls())
fileName = commandArgs(trailingOnly = TRUE)
noExtension = tools::file_path_sans_ext(fileName)
# print(noExtension)
defaultDataDir = "../Data/" 
fileLocation = file.path(defaultDataDir, fileName)
trees_data = read.csv(fileLocation, header = T)

# -------------------------------------------- Create TreeHeight Function -------------------------------------------- 
TreeHeight <- function(degrees, distance) {
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  print(height)

  return(height)
}

# -------------------------------------------- Apply TreeHeight Function -------------------------------------------- 
trees_data$Height = TreeHeight(trees_data$Angle.degrees, trees_data$Distance.m)

# -------------------------------------------- Save the output file as csv format -------------------------------------------- 
write.csv(trees_data, paste("../Results/", noExtension, "_treeheights.csv", sep = ""), row.names = F)
cat("The file has been saved in ", "../Results/", noExtension, "_treeheights.csv\n", sep = "")
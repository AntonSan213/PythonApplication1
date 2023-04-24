inputs =[2,6,8,0]
         
weights = [[0.2,-0.12,0.7,1.0],
          [0.3,0.7,-1.0,0.1],
          [0.98,-0.15,0.89,0.75]]
bias = [7,3,9];
def layers(inputs,weights,bias):
    list_output=[]
    for cur_wght,cur_bias in zip(weights,bias):
        output = 0;
        for i,w in zip(inputs,cur_wght,):
            output+=i*w
        output+=cur_bias
        list_output.append(output)
    return list_output

layer_1 = layers(inputs,weights,bias)
layer_2 = layers(layer_1,weights,bias)
layer_3 = layers(layer_2,weights,bias)
print(layer_1)
print(layer_2)
print(layer_3)
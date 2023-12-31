import numpy as np

def zigzag(input):
    # Initializing the variables
    # ----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    vmax = input.shape[0]
    hmax = input.shape[1]

    i = 0

    output = np.zeros((vmax * hmax))
    # ----------------------------------

    while ((v < vmax) and (h < hmax)):

        if ((h + v) % 2) == 0:  # Going up

            if (v == vmin):
                output[i] = input[v, h]  # If we got to the first line

                if (h == hmax):
                    v = v + 1
                else:
                    h = h + 1

                i = i + 1

            elif ((h == hmax - 1) and (v < vmax)):  # If we got to the last column
                output[i] = input[v, h]
                v = v + 1
                i = i + 1

            elif ((v > vmin) and (h < hmax - 1)):  # All other cases
                output[i] = input[v, h]
                v = v - 1
                h = h + 1
                i = i + 1


        else:  # Going down

            if ((v == vmax - 1) and (h <= hmax - 1)):  # If we got to the last line
                output[i] = input[v, h]
                h = h + 1
                i = i + 1

            elif (h == hmin):  # If we got to the first column
                output[i] = input[v, h]

                if (v == vmax - 1):
                    h = h + 1
                else:
                    v = v + 1

                i = i + 1

            elif ((v < vmax - 1) and (h > hmin)):  # All other cases
                output[i] = input[v, h]
                v = v + 1
                h = h - 1
                i = i + 1

        if ((v == vmax - 1) and (h == hmax - 1)):  # Bottom right element
            output[i] = input[v, h]
            break

    return output


def inverse_zigzag(input, vmax, hmax):
    # Initializing the variables
    # ----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    output = np.zeros((vmax, hmax))

    i = 0
    # ----------------------------------

    while ((v < vmax) and (h < hmax)):
        if ((h + v) % 2) == 0:  # Going up

            if (v == vmin):
                output[v, h] = input[i]  # If we got to the first line

                if (h == hmax):
                    v = v + 1
                else:
                    h = h + 1

                i = i + 1

            elif ((h == hmax - 1) and (v < vmax)):  # If we got to the last column
                output[v, h] = input[i]
                v = v + 1
                i = i + 1

            elif ((v > vmin) and (h < hmax - 1)):  # All other cases
                output[v, h] = input[i]
                v = v - 1
                h = h + 1
                i = i + 1


        else:  # Going down

            if ((v == vmax - 1) and (h <= hmax - 1)):  # If we got to the last line
                output[v, h] = input[i]
                h = h + 1
                i = i + 1

            elif (h == hmin):  # If we got to the first column
                output[v, h] = input[i]

                if (v == vmax - 1):
                    h = h + 1
                else:
                    v = v + 1

                i = i + 1

            elif ((v < vmax - 1) and (h > hmin)):  # All other cases
                output[v, h] = input[i]
                v = v + 1
                h = h - 1
                i = i + 1

        if ((v == vmax - 1) and (h == hmax - 1)):  # Bottom right element
            output[v, h] = input[i]
            break

    return output

/* 30/08/2017 */
#include <stdio.h>
#include <inttypes.h>

int main(void){
    uint8_t s[64] = {0};
    int l = 64*3;

    for(int c, i = 0; (c = getchar()) != EOF; i++){
        if(c == '\n' && i < l)
            l = i+1;
        else if(c == 'O')
            s[(i%l)/3] |= (1 << (2*(i/l) + i%3));
    }

    for(int i = 0; i < l/3; i++)
        putchar("_a_c_bif_e_d_hjg_k_m_lsp_o_n_rtq______________w__u_x_v___z_y__"[s[i]]);
}
